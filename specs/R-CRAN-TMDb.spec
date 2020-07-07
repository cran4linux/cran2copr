%global packname  TMDb
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}
Summary:          Access to TMDb API

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-stringi >= 1.4.6
BuildRequires:    R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-stringi >= 1.4.6
Requires:         R-CRAN-httr >= 1.4.1

%description
Provides an R-interface to the TMDb API (see TMDb API on
<https://developers.themoviedb.org/3/getting-started/introduction>). The
Movie Database (TMDb) is a popular user editable database for movies and
TV shows (see <https://www.themoviedb.org>).

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
