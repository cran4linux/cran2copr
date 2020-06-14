%global packname  nnfor
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          2%{?dist}
Summary:          Time Series Forecasting with Neural Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-neuralnet 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-tsutils 
BuildRequires:    R-CRAN-uroot 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-neuralnet 
Requires:         R-CRAN-plotrix 
Requires:         R-MASS 
Requires:         R-CRAN-tsutils 
Requires:         R-CRAN-uroot 

%description
Automatic time series modelling with neural networks. Allows fully
automatic, semi-manual or fully manual specification of networks. For
details of the specification methodology see: (i) Crone and Kourentzes
(2010) <doi:10.1016/j.neucom.2010.01.017>; and (ii) Kourentzes et al.
(2014) <doi:10.1016/j.eswa.2013.12.011>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
