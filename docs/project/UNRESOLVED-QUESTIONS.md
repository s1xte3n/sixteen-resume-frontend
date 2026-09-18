// UNRESOLVED-QUESTIONS.md

# Azure Cloud Resume Challenge — Unresolved Questions

Discovery is complete. There are no remaining high-impact product or scope questions blocking implementation.

The remaining items are implementation-time decisions rather than unresolved project requirements.

## 1. Final FreeDNS Hostname

**Impact:** Low

The DNS provider has been selected, but the exact hostname has not yet been created.

**Resolution timing:** During DNS setup.

---

## 2. Final Resume Content

**Impact:** Medium

The source CV is available, but it still needs to be edited and converted into the final HTML resume.

Known positioning decision:

> 4+ years of hands-on software development experience

Professional employment remains:

> IT Operator — Gijima Holdings | June 2022–Present

**Resolution timing:** During frontend implementation.

---

## 3. Final Visual Design

**Impact:** Low

No visual design preference has been specified.

**Decision:** Keep the initial design simple and professional and avoid adding unnecessary design scope.

**Resolution timing:** During HTML/CSS implementation.

---

## 4. Blog URLs

**Impact:** Low

The platforms have been selected:

* Dev.to
* Hashnode

The actual article URLs do not exist yet.

**Resolution timing:** After the project implementation is sufficiently complete to document the journey.

---

## 5. Exact GitHub Actions Authentication Mechanism

**Impact:** Low

The project requires secure CI/CD credentials but does not yet specify the exact authentication mechanism.

**Constraint:** Azure credentials must never be committed to either repository.

**Resolution timing:** During CI/CD implementation.

---

## 6. Exact ARM Resource Configuration

**Impact:** Low

The required Azure services are known, but exact resource names, settings, SKU details, and template parameters have not yet been established.

**Resolution timing:** During infrastructure implementation.

---

## 7. CDN Cache Purging Strategy

**Impact:** Low

The frontend deployment may require CDN cache invalidation after Storage updates.

**Resolution:** Determine the minimum-cost and simplest approach during CI/CD implementation.

---

## 8. AZ-900 Certification

**Impact:** Medium, but not an implementation blocker

The challenge explicitly specifies AZ-900, while the user currently has AI-901.

**Current decision:** Use AI-901 and document the deviation.

If AZ-900 is obtained later, the resume and project documentation can be updated.

---

## Discovery Closure

The following previously unresolved items are now resolved:

* DNS provider → FreeDNS / afraid.org
* Azure certification → AI-901 currently held
* Resume source → Complete CV supplied
* Resume experience positioning → 4+ years hands-on software development
* Backend repository → `sixteen-resume-backend`
* Frontend repository → `sixteen-resume-frontend`
* Blog platforms → Dev.to + Hashnode
* Blog scope → Technical lessons + complete project journey
* Azure subscription → Existing subscription
* Azure region → East US
* Deployment count → One
* Cost strategy → R0 where possible, otherwise lowest possible cost
* Visual design → No predefined preference
* Deadline → 30 September 2026

**Discovery status: COMPLETE**
