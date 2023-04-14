%global __brp_check_rpaths %{nil}
%global packname  neuroim
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Data Structures and Handling for Neuroimaging Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-yaImpute 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rgl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-hash 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-CRAN-yaImpute 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rgl 

%description
A collection of data structures that represent volumetric brain imaging
data. The focus is on basic data handling for 3D and 4D neuroimaging data.
In addition, there are function to read and write NIFTI files and limited
support for reading AFNI files.

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
