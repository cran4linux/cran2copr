%global __brp_check_rpaths %{nil}
%global packname  sparseLDA
%global packver   0.1-9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          3%{?dist}%{?buildtag}
Summary:          Sparse Discriminant Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mda 
Requires:         R-CRAN-elasticnet 
Requires:         R-MASS 
Requires:         R-CRAN-mda 

%description
Performs sparse linear discriminant analysis for Gaussians and mixture of
Gaussian models.

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
