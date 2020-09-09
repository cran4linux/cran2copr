%global packname  shinylogs
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Record Everything that Happens in a 'Shiny' Application

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny >= 1.1.0
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-nanotime 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-anytime 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-shiny >= 1.1.0
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-nanotime 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-anytime 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-RSQLite 

%description
Track and record the use of applications and the user's interactions with
'Shiny' inputs. Allow to save inputs clicked, output generated and
eventually errors.

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
