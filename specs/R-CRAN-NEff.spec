%global packname  NEff
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          2%{?dist}
Summary:          Calculating Effective Sizes Based on Known DemographicParameters of a Population

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-bit 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-bit 

%description
Effective population sizes (often abbreviated as "Neff") are essential in
biodiversity monitoring and conservation. For the first time, calculating
effective sizes with data obtained within less than a generation but
considering demographic parameters is possible. This individual based
model uses demographic parameters of a population to calculate annual
effective sizes and effective population sizes (per generation). A defined
number of alleles and loci will be used to simulate the genotypes of the
individuals. Stepwise mutation rates can be included. Variations in life
history parameters (sex ratio, sex-specific survival, recruitment rate,
reproductive skew) are possible. These results will help managers to
define existing populations as viable or not.

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
%{rlibdir}/%{packname}/INDEX
