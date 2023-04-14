%global __brp_check_rpaths %{nil}
%global packname  bhpm
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Bayesian Hierarchical Poisson Models for Multiple GroupedOutcomes with Clustering

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-coda 

%description
Bayesian hierarchical methods for the detection of differences in rates of
related outcomes for multiple treatments for clustered observations.
Theoretical background for the models is given in Carragher (2017)
<https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.736866>. The models
in this package are extensions for multiple treatments and clusters. This
software was developed for the Precision Drug Theraputics: Risk Prediction
in Pharmacoepidemiology project as part of a Rutherford Fund Fellowship at
Health Data Research (UK), Medical Research Council (UK) award reference
MR/S003967/1 (<https://gtr.ukri.org/>). Principal Investigator: Raymond
Carragher.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
