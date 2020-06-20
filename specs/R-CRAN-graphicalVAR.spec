%global packname  graphicalVAR
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}
Summary:          Graphical VAR for Experience Sampling Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-qgraph >= 1.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-qgraph >= 1.3.1
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-Matrix 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-igraph 

%description
Estimates within and between time point interactions in experience
sampling data, using the Graphical vector autoregression model in
combination with regularization. See also Epskamp, Waldorp, Mottus &
Borsboom (2018) <doi:10.1080/00273171.2018.1454823>.

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
