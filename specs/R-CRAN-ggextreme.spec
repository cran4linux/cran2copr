%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ggextreme
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bar Chart Races and Interactive Plots for Clinical Research

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-systemfonts >= 1.2.4
BuildRequires:    R-CRAN-ggiraph >= 0.9.6
BuildRequires:    R-CRAN-gdtools >= 0.5.0
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ragg 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-systemfonts >= 1.2.4
Requires:         R-CRAN-ggiraph >= 0.9.6
Requires:         R-CRAN-gdtools >= 0.5.0
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-jsonlite 
Requires:         R-parallel 
Requires:         R-CRAN-ragg 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Presentation quality charts built on 'ggplot2' that the package itself
does not provide. The bar chart race interpolates values on a uniform time
grid, ranks every frame on its own values and eases bars into new
positions, so a reordering field stays readable. Frames are ordinary
'ggplot2' objects laid out on a fixed pixel grid, which keeps the axis and
label column from drifting between them, and are encoded to GIF or MP4.
Circular images, such as the bundled country flags, can be placed at the
end of each bar. Causal diagrams are drawn as directed acyclic graphs
whose nodes and arrows each carry a rationale and references, shown on
hover and opened with clickable links on click, through 'ggiraph'; the
same diagram is also available as a static 'ggplot2' object. Network plots
for network meta-analysis are drawn from arm level data, with the baseline
characteristics and outcomes of every arm shown side by side on click.
Forest plots for 'metafor' and 'meta' fits carry each study's record and
risk of bias traffic lights, and replay a cumulative meta-analysis as an
animation; funnel plots shade where each study would be significant and
carry the pooled estimate without it, trim and fill and the tests for
small-study effects; league tables for 'netmeta' fits show the direct and
indirect evidence behind every estimate. Kaplan-Meier plots read survival
and the hazard ratio at any time under the pointer, beside a risk table
and proportional hazards tests, and swimmer plots give each patient a lane
with their responses, progression and death. Nomograms of regression
models, from linear and generalized linear models to mixed, Cox,
parametric survival, ordinal and multinomial models, have a handle per
predictor and compute each prediction with its confidence interval in the
page. Choropleth maps of the world or of any 'sf' map step or play through
the years, with several measures side by side for the same year. Causal
diagrams can also show which paths between an exposure and an outcome an
adjustment set leaves open, by the backdoor criterion; Kaplan-Meier plots
give the restricted mean survival time up to a horizon the reader can
move; league tables and network plots show where each network estimate's
evidence comes from; and swimmer plots can carry a waterfall of best
change and each patient's course beside the lanes. Four explorers put a
threshold or an assumption in the reader's hands: the cutoff of a
diagnostic test, with what it means for 1,000 people at any prevalence;
the strength of unmeasured confounding, with E-values; the choices of a
multiverse of analyses; and the threshold that defines a responder. Plots
after CINeMA judge the confidence in each estimate of a network
meta-analysis in six domains, with every judgment's reason and source, and
show what lies behind them: each study's contribution, the estimates
against a movable range of little difference, direct against indirect
evidence, and a league table and a network marked with the judgments.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
