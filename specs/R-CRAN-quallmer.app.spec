%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quallmer.app
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Validation App for 'quallmer'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-quallmer >= 0.3.0
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-quallmer >= 0.3.0
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-cli 
Requires:         R-stats 
Requires:         R-utils 

%description
Companion package to 'quallmer' providing an interactive 'shiny'
application for manual coding, reviewing large language model (LLM)
generated annotations, and computing inter-rater reliability metrics.
Supports three modes: blind manual coding, LLM output validation, and
agreement calculation. Computes standard reliability metrics including
Krippendorff's alpha (Krippendorff 2019 <doi:10.4135/9781071878781>),
Cohen's kappa, Fleiss' kappa (Fleiss 1971 <doi:10.1037/h0031619>),
intraclass correlation coefficient (ICC), and percent agreement for
nominal, ordinal, interval, and ratio data. Also computes gold-standard
validation metrics including accuracy, precision, recall, and F1 scores
following Sokolova and Lapalme (2009 <doi:10.1016/j.ipm.2009.03.002>).

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
