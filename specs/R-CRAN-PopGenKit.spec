%global packname  PopGenKit
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Useful functions for (batch) file conversion and data resamplingin microsatellite datasets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
There are two main purposes to this package. The first is to allow batch
conversion of Genepop (Rousset 2008) input files for use with Arlequin
(Excoffier and Lischer 2010), which has a simple GUI to analyze batch
files. Two commonly used simulation software, BottleSim (Kuo & Janzen
2003) and Easypop (Balloux 2001) produce Genepop output files that can be
analyzed this way. There are also functions to convert to and from
BottleSim format, to quickly produce allele frequency tables or to convert
a file directly for use in ordination analyses (e.g. principal component
analysis). This package also includes functions to calculate allele
rarefaction curves, confidence intervals on heterozygosity and allelic
richness with resampling strategies (bootstrap and jackknife).

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
