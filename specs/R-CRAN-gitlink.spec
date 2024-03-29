%global __brp_check_rpaths %{nil}
%global packname  gitlink
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Add 'Git' Links to Your Web Based Assets

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-rlang >= 0.3.1
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-rlang >= 0.3.1

%description
Provides helpers to add 'Git' links to 'shiny' applications, 'rmarkdown'
documents, and other 'HTML' based resources. This is most commonly used
for 'GitHub' ribbons.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
