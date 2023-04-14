%global __brp_check_rpaths %{nil}
%global packname  rgoogleslides
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          R Interface to Google Slides

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-R6 

%description
Previously, when one is working with in the Google Ecosystem (Using Google
Drive etc), there is hardly any good workflow of getting the values
calculated from R and getting that into Google Slides. The normal and easy
way out would be to just copy your work over but when you have a number of
analysis to present with a lot of changes between each environment, it
just becomes quite cumbersome.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
