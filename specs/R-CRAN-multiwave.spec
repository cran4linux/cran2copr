%global packname  multiwave
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Estimation of Multivariate Long-Memory Models Parameters

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Computation of an estimation of the long-memory parameters and the
long-run covariance matrix using a multivariate model (Lobato (1999)
<doi:10.1016/S0304-4076(98)00038-4>; Shimotsu (2007)
<doi:10.1016/j.jeconom.2006.01.003>). Two semi-parametric methods are
implemented: a Fourier based approach (Shimotsu (2007)
<doi:10.1016/j.jeconom.2006.01.003>) and a wavelet based approach (Achard
and Gannaz (2016) <doi:10.1111/jtsa.12170>).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
