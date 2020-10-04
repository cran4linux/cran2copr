%global packname  variantspark
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          A 'Sparklyr' Extension for 'VariantSpark'

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sparklyr >= 1.0.1
Requires:         R-CRAN-sparklyr >= 1.0.1

%description
This is a 'sparklyr' extension integrating 'VariantSpark' and R.
'VariantSpark' is a framework based on 'scala' and 'spark' to analyze
genome datasets, see <https://bioinformatics.csiro.au/>. It was tested on
datasets with 3000 samples each one containing 80 million features in
either unsupervised clustering approaches and supervised applications,
like classification and regression. The genome datasets are usually
writing in VCF, a specific text file format used in bioinformatics for
storing gene sequence variations. So, 'VariantSpark' is a great tool for
genome research, because it is able to read VCF files, run analyses and
return the output in a 'spark' data frame.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/INDEX
