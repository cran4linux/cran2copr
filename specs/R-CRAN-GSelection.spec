%global __brp_check_rpaths %{nil}
%global packname  GSelection
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Genomic Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-SAM 
BuildRequires:    R-CRAN-penalized 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-SAM 
Requires:         R-CRAN-penalized 
Requires:         R-CRAN-gdata 
Requires:         R-stats 
Requires:         R-utils 

%description
Genomic selection is a specialized form of marker assisted selection. The
package contains functions to select important genetic markers and predict
phenotype on the basis of fitted training data using integrated model
framework (Guha Majumdar et. al. (2019) <doi:10.1089/cmb.2019.0223>)
developed by combining one additive (sparse additive models by Ravikumar
et. al. (2009) <doi:10.1111/j.1467-9868.2009.00718.x>) and one
non-additive (hsic lasso by Yamada et. al. (2014)
<doi:10.1162/NECO_a_00537>) model.

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
