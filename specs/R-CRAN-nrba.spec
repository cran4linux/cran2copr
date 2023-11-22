%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nrba
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Methods for Conducting Nonresponse Bias Analysis (NRBA)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-survey >= 4.1.1
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-svrep 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-survey >= 4.1.1
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-srvyr 
Requires:         R-stats 
Requires:         R-CRAN-svrep 
Requires:         R-CRAN-tidyr 

%description
Facilitates nonresponse bias analysis (NRBA) for survey data.  Such data
may arise from a complex sampling design with features such as
stratification, clustering, or unequal probabilities of selection.
Multiple types of analyses may be conducted: comparisons of response rates
across subgroups; comparisons of estimates before and after weighting
adjustments; comparisons of sample-based estimates to external population
totals; tests of systematic differences in covariate means between
respondents and full samples; tests of independence between response
status and covariates; and modeling of outcomes and response status as a
function of covariates. Extensive documentation and references are
provided for each type of analysis. Krenzke, Van de Kerckhove, and
Mohadjer (2005)
<http://www.asasrms.org/Proceedings/y2005/files/JSM2005-000572.pdf> and
Lohr and Riddles (2016)
<https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2016002/article/14677-eng.pdf?st=q7PyNsGR>
provide an overview of the methods implemented in this package.

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
