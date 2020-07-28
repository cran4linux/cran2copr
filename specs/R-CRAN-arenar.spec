%global packname  arenar
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}
Summary:          Arena for the Exploration and Comparison of any ML Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-DALEX >= 1.3.0
BuildRequires:    R-CRAN-ingredients 
BuildRequires:    R-CRAN-iBreakDown 
BuildRequires:    R-CRAN-gistr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-plumber 
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-auditor 
Requires:         R-CRAN-DALEX >= 1.3.0
Requires:         R-CRAN-ingredients 
Requires:         R-CRAN-iBreakDown 
Requires:         R-CRAN-gistr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-plumber 
Requires:         R-parallel 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-auditor 

%description
Generates data for challenging machine learning models in 'Arena'
<https://arena.drwhy.ai> - an interactive web application. You can start
the server with XAI (Explainable Artificial Intelligence) plots to be
generated on-demand or precalculate and auto-upload data file beside
shareable 'Arena' URL.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
