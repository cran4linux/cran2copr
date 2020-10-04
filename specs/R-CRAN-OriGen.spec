%global packname  OriGen
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          3%{?dist}%{?buildtag}
Summary:          Fast Spatial Ancestry via Flexible Allele Frequency Surfaces

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-ggplot2 

%description
Used primarily for estimates of allele frequency surfaces from point
estimates. It can also place individuals of unknown origin back onto the
geographic map with great accuracy. Additionally, it can place admixed
individuals by estimating contributing fractions at each location on a
map. Lastly, it can rank SNPs by their ability to differentiate
populations. See "Fast Spatial Ancestry via Flexible Allele Frequency
Surfaces" (John Michael Ranola, John Novembre, Kenneth Lange) in
Bioinformatics 2014 for more info.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
