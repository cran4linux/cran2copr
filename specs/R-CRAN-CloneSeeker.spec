%global packname  CloneSeeker
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          3%{?dist}%{?buildtag}
Summary:          Seeking and Finding Clones in Copy Number and Sequencing Data

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-quantmod 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-quantmod 

%description
Defines the classes and functions used to simulate and to analyze data
sets describing copy number variants and, optionally, sequencing mutations
in order to detect clonal subsets. See Zucker et al. (2019)
<doi:10.1093/bioinformatics/btz057>.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/auxiliary
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
