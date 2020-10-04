%global packname  prodigenr
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          3%{?dist}%{?buildtag}
Summary:          Research Project Directory Generator

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 1.9
BuildRequires:    R-CRAN-rprojroot >= 1.3.2
BuildRequires:    R-CRAN-usethis >= 1.3.0
BuildRequires:    R-CRAN-fs >= 1.2.2
BuildRequires:    R-CRAN-git2r >= 0.21.0
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-rmarkdown >= 1.9
Requires:         R-CRAN-rprojroot >= 1.3.2
Requires:         R-CRAN-usethis >= 1.3.0
Requires:         R-CRAN-fs >= 1.2.2
Requires:         R-CRAN-git2r >= 0.21.0
Requires:         R-CRAN-withr 

%description
Create a project directory structure, along with typical files for that
project.  This allows projects to be quickly and easily created, as well
as for them to be standardized. Designed specifically with scientists in
mind (mainly bio-medical researchers, but likely applies to other fields).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rmarkdown
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
