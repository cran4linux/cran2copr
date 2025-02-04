%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MplusLGM
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automate Latent Growth Mixture Modelling in 'Mplus'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MplusAutomation 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-parallel 
Requires:         R-CRAN-MplusAutomation 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 
Requires:         R-parallel 

%description
Provide a suite of functions for conducting and automating Latent Growth
Modeling (LGM) in 'Mplus', including Growth Curve Model (GCM),
Growth-Based Trajectory Model (GBTM) and Latent Class Growth Analysis
(LCGA). The package builds upon the capabilities of the 'MplusAutomation'
package (Hallquist & Wiley, 2018) to streamline large-scale latent
variable analyses. “MplusAutomation: An R Package for Facilitating
Large-Scale Latent Variable Analyses in Mplus.” Structural Equation
Modeling, 25(4), 621–638. <doi:10.1080/10705511.2017.1402334> The workflow
implemented in this package follows the recommendations outlined in Van
Der Nest et al. (2020). “An Overview of Mixture Modeling for Latent
Evolutions in Longitudinal Data: Modeling Approaches, Fit Statistics, and
Software.” Advances in Life Course Research, 43, Article 100323.
<doi:10.1016/j.alcr.2019.100323>.

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
