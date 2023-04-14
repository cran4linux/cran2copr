%global __brp_check_rpaths %{nil}
%global packname  M2SMF
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Multi-Modal Similarity Matrix Factorization for IntegrativeMulti-Omics Data Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-MASS 
Requires:         R-stats 

%description
A new method to implement clustering from multiple modality data of
certain samples, the function M2SMF() jointly factorizes multiple
similarity matrices into a shared sub-matrix and several modality private
sub-matrices, which is further used for clustering. Along with this
method, we also provide function to calculate the similarity matrix and
function to evaluate the best cluster number from the original data.

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
