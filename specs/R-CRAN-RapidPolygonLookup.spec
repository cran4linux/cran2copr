%global __brp_check_rpaths %{nil}
%global packname  RapidPolygonLookup
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          POLYGON LOOKUP USING KD TREES

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-PBSmapping 
BuildRequires:    R-CRAN-RgoogleMaps 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-PBSmapping 
Requires:         R-CRAN-RgoogleMaps 

%description
Facilitates efficient polygon search using kd trees. Coordinate level
spatial data can be aggregated to higher geographical identities like
census blocks, ZIP codes or police district boundaries. This process
requires mapping each point in the given data set to a particular identity
of the desired geographical hierarchy. Unless efficient data structures
are used, this can be a daunting task. The operation point.in.polygon()
from the package sp is computationally expensive. Here, we exploit
kd-trees as efficient nearest neighbor search algorithm to dramatically
reduce the effective number of polygons being searched.

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
