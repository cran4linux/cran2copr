%global packname  Hapi
%global packver   0.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Inference of Chromosome-Length Haplotypes Using Genomic Data ofSingle Gamete Cells

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-HMM 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-HMM 
Requires:         R-CRAN-ggplot2 

%description
Inference of chromosome-length haplotypes using a few haploid gametes of
an individual. The gamete genotype data may be generated from various
platforms including genotyping arrays and sequencing even with
low-coverage. Hapi simply takes genotype data of known hetSNPs in single
gamete cells as input and report the high-resolution haplotypes as well as
confidence of each phased hetSNPs. The package also includes a module
allowing downstream analyses and visualization of identified crossovers in
the gametes.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
