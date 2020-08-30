%global packname  cabinets
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Project Specific Workspace Organization Templates

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-cli 

%description
Creates project specific directory and file templates that are written to
a .Rprofile file. Upon starting a new R session, these templates can be
used to streamline the creation of new directories that are standardized
to the user's preferences.

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
