%global packname  brranching
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          2%{?dist}%{?buildtag}
Summary:          Fetch 'Phylogenies' from Many Sources

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-taxize >= 0.9.97
BuildRequires:    R-CRAN-crul >= 0.4.0
BuildRequires:    R-CRAN-phylocomr >= 0.1.4
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-conditionz 
Requires:         R-CRAN-taxize >= 0.9.97
Requires:         R-CRAN-crul >= 0.4.0
Requires:         R-CRAN-phylocomr >= 0.1.4
Requires:         R-CRAN-curl 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-conditionz 

%description
Includes methods for fetching 'phylogenies' from a variety of sources,
including the 'Phylomatic' web service
(<http://phylodiversity.net/phylomatic>), and 'Phylocom'
(<https://github.com/phylocom/phylocom/>).

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
