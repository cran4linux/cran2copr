%global packname  binnednp
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          1%{?dist}
Summary:          Nonparametric Estimation for Interval-Grouped Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-kedd 
BuildRequires:    R-CRAN-nor1mix 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-kedd 
Requires:         R-CRAN-nor1mix 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-Rdpack 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Kernel density and distribution estimation for interval-grouped data
(Reyes, Francisco-Fernandez and Cao 2016, 2017)
<doi:10.1080/10485252.2016.1163348>, <doi:10.1007/s11749-017-0523-9>,
(Gonzalez-Andujar, Francisco-Fernandez, Cao, Reyes, Urbano, Forcella and
Bastida 2016) <doi:10.1111/wre.12216> and nonparametric estimation of
seedling emergence indices (Cao, Francisco-Fernandez, Anand, Bastida and
Gonzalez-Andujar 2011) <doi:10.1017/S002185961100030X>.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
