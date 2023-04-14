%global __brp_check_rpaths %{nil}
%global packname  roots
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Reconstructing Ordered Ontogenic Trajectories

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-animation >= 2.4
BuildRequires:    R-CRAN-igraph >= 1.0.0
BuildRequires:    R-CRAN-rARPACK >= 0.11.0
Requires:         R-CRAN-animation >= 2.4
Requires:         R-CRAN-igraph >= 1.0.0
Requires:         R-CRAN-rARPACK >= 0.11.0

%description
A set of tools to reconstruct ordered ontogenic trajectories from single
cell RNAseq data.

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
