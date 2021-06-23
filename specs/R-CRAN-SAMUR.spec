%global __brp_check_rpaths %{nil}
%global packname  SAMUR
%global packver   0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Stochastic Augmentation of Matched Data Using RestrictionMethods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Matching 
Requires:         R-CRAN-Matching 

%description
Augmenting a matched data set by generating multiple stochastic, matched
samples from the data using a multi-dimensional histogram constructed from
dropping the input matched data into a multi-dimensional grid built on the
full data set. The resulting stochastic, matched sets will likely provide
a collectively higher coverage of the full data set compared to the single
matched set. Each stochastic match is without duplication, thus allowing
downstream validation techniques such as cross-validation to be applied to
each set without concern for overfitting.

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
