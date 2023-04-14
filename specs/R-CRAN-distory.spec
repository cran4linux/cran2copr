%global __brp_check_rpaths %{nil}
%global packname  distory
%global packver   1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          3%{?dist}%{?buildtag}
Summary:          Distance Between Phylogenetic Histories

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape >= 5.0
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-ape >= 5.0
Requires:         R-graphics 
Requires:         R-stats 

%description
Geodesic distance between phylogenetic trees and associated functions. The
theoretical background of 'distory' is published in Billera et al. (2001)
"Geometry of the space of phylogenetic trees."
<doi:10.1006/aama.2001.0759>.

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
