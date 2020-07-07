%global packname  ICAOD
%global packver   0.9.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.9
Release:          2%{?dist}
Summary:          Optimal Designs for Nonlinear Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-cubature 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvQuad 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-nloptr 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-cubature 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-mnormt 
Requires:         R-methods 
Requires:         R-CRAN-mvQuad 

%description
Finds optimal designs for nonlinear models using a metaheuristic algorithm
called imperialist competitive algorithm ICA. See, for details, Masoudi et
al. (2017) <doi:10.1016/j.csda.2016.06.014> and Masoudi et al. (2019)
<doi:10.1080/10618600.2019.1601097>.

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
