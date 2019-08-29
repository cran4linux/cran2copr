%global packname  adhoc
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Calculate Ad Hoc Distance Thresholds for DNA BarcodingIdentification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-CRAN-polynom 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-pegas 
Requires:         R-CRAN-polynom 

%description
Two functions to calculate intra- and interspecific pairwise distances,
evaluate DNA barcoding identification error and calculate an ad hoc
distance threshold for each particular reference library of DNA barcodes.
Specimen identification at this ad hoc distance threshold (using the best
close match method) will produce identifications with an estimated
relative error probability that can be fixed by the user (e.g. 5%).

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
