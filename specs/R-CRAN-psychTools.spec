%global packname  psychTools
%global packver   1.9.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.12
Release:          2%{?dist}
Summary:          Tools to Accompany the 'psych' Package for PsychologicalResearch

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-psych 
Requires:         R-foreign 
Requires:         R-CRAN-psych 

%description
Support functions, data sets, and vignettes for the 'psych' package.
Contains several of the biggest data sets for the 'psych' package as well
as one vignette. A few helper functions for file manipulation are included
as well. For more information, see the <https://personality-project.org/r>
web page.

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

%files
%{rlibdir}/%{packname}
