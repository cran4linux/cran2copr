%global __brp_check_rpaths %{nil}
%global packname  LaF
%global packver   0.8.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.4
Release:          3%{?dist}%{?buildtag}
Summary:          Fast Access to Large ASCII Files

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.1
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.11.1
Requires:         R-methods 
Requires:         R-utils 

%description
Methods for fast access to large ASCII files.  Currently the following
file formats are supported: comma separated format (CSV) and fixed width
format. It is assumed that the files are too large to fit into memory,
although the package can also be used to efficiently access files that do
fit into memory. Methods are provided to access and process files
blockwise. Furthermore, an opened file can be accessed as one would an
ordinary data.frame. The LaF vignette gives an overview of the
functionality provided.

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
