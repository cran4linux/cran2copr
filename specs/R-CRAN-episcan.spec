%global __brp_check_rpaths %{nil}
%global packname  episcan
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Scan Pairwise Epistasis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch

%description
Searching genomic interactions with linear/logistic regression in a
high-dimensional dataset is a time-consuming task. This package provides
some efficient ways to scan epistasis in genome-wide interaction studies
(GWIS). Both case-control status (binary outcome) and quantitative
phenotype (continuous outcome) are supported (the main references: 1.
Kam-Thong, T., D. Czamara, K. Tsuda, K. Borgwardt, C. M. Lewis, A.
Erhardt-Lehmann, B. Hemmer, et al. (2011). <doi:10.1038/ejhg.2010.196>. 2.
Kam-Thong, T., B. Pütz, N. Karbalai, B. Müller-Myhsok, and K. Borgwardt.
(2011).  <doi:10.1093/bioinformatics/btr218>.)

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
