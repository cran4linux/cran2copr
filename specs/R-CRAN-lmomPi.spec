%global packname  lmomPi
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          (Precipitation) Frequency Analysis and Variability withL-Moments from 'lmom'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lmom 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-lmom 
Requires:         R-CRAN-stringr 

%description
It is an extension of 'lmom' R package: 'pel','cdf',qua' function families
are lumped and called from one function per each family respectively in
order to create robust automatic tools to fit data with different
probability distributions and then to estimate probability values and
return periods.  The implemented functions are able to manage time series
with constant and/or missing values without stopping the execution with
error messages. The package also contains tools to calculate several
indices based on variability (e.g. 'SPI' , Standardized Precipitation
Index, see
<https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-index-spi>
and <http://spei.csic.es/>) for multiple time series or spatio-temporal
gridded values.

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
%doc %{rlibdir}/%{packname}/script.R
%{rlibdir}/%{packname}/INDEX
