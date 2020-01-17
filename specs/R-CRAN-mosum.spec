%global packname  mosum
%global packver   1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Moving Sum Based Procedures for Changes in the Mean

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-plot3D 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-plot3D 

%description
Implementations of MOSUM-based statistical procedures and algorithms for
detecting multiple changes in the mean. This comprises the MOSUM procedure
for estimating multiple mean changes from Eichinger and Kirch (2018)
<doi:10.3150/16-BEJ887> and the multiscale algorithmic extensions from Cho
and Kirch (2019) <arXiv:1910.12486>.

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
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
