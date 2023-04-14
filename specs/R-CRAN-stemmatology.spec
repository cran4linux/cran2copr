%global __brp_check_rpaths %{nil}
%global packname  stemmatology
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          3%{?dist}%{?buildtag}
Summary:          Stemmatological Analysis of Textual Traditions

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-xml2 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-cluster 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-xml2 

%description
Explore and analyse the genealogy of textual or musical traditions, from
their variants, with various stemmatological methods, mainly the
disagreement-based algorithms suggested by Camps and Cafiero (2015)
<doi:10.1484/M.LECTIO-EB.5.102565>.

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
