%global packname  MetProc
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Separate Metabolites into Likely Measurement Artifacts and TrueMetabolites

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-fastcluster 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-fastcluster 

%description
Split an untargeted metabolomics data set into a set of likely true
metabolites and a set of likely measurement artifacts. This process
involves comparing missing rates of pooled plasma samples and biological
samples. The functions assume a fixed injection order of samples where
biological samples are randomized and processed between intermittent
pooled plasma samples. By comparing patterns of missing data across
injection order, metabolites that appear in blocks and are likely
artifacts can be separated from metabolites that seem to have random
dispersion of missing data. The two main metrics used are: 1. the number
of consecutive blocks of samples with present data and 2. the correlation
of missing rates between biological samples and flanking pooled plasma
samples.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
