%global __brp_check_rpaths %{nil}
%global packname  GFDsurv
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Tests for Survival Data in General Factorial Designs

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.53
BuildRequires:    R-CRAN-survival >= 3.2.7
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-shinyjs >= 2.0.0
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-magic >= 1.5.9
BuildRequires:    R-CRAN-shiny >= 1.5.0
BuildRequires:    R-CRAN-shinythemes >= 1.1.2
BuildRequires:    R-CRAN-shinyWidgets >= 0.5.4
BuildRequires:    R-CRAN-survminer >= 0.4.8
BuildRequires:    R-CRAN-tippy >= 0.1.0
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS >= 7.3.53
Requires:         R-CRAN-survival >= 3.2.7
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-shinyjs >= 2.0.0
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-magic >= 1.5.9
Requires:         R-CRAN-shiny >= 1.5.0
Requires:         R-CRAN-shinythemes >= 1.1.2
Requires:         R-CRAN-shinyWidgets >= 0.5.4
Requires:         R-CRAN-survminer >= 0.4.8
Requires:         R-CRAN-tippy >= 0.1.0
Requires:         R-stats 

%description
Implemented are three Wald-type statistic and respective permuted versions
for null hypotheses formulated in terms of cumulative hazard rate
functions, medians and the concordance measure, respectively, in the
general framework of survival factorial designs with possibly
heterogeneous survival and/or censoring distributions, for crossed designs
with an arbitrary number of factors and nested designs with up to three
factors. Ditzhaus, Dobler and Pauly (2020) <doi:10.1177/0962280220980784>
Ditzhaus, Janssen, Pauly (2020) <arXiv: 2004.10818v2> Dobler and Pauly
(2019) <doi:10.1177/0962280219831316>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
