%global packname  TipDatingBeast
%global packver   1.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          3%{?dist}
Summary:          Using Tip Dates with Phylogenetic Trees in BEAST

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-TeachingDemos 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-TeachingDemos 
Requires:         R-CRAN-DescTools 
Requires:         R-utils 
Requires:         R-stats 

%description
Assists performing tip-dating of phylogenetic trees with BEAST BEAST is a
popular software for phylogenetic analysis. The package assists the
implementation of various phylogenetic tip- dating tests using BEAST. It
contains two main functions. The first one allows preparing date
randomization analyses, which assess the temporal signal of a data set.
The second function allows performing leave-one-out analyses, which test
for the consistency between independent calibration sequences and allow
pinpointing those leading to potential bias. The included tutorial
provides detailed step-by-step instructions. An expanded description of
the package can be found in article: Rieux, A. and Khatchikian, C.E.
(2017), TIPDATINGBEAST: an R package to assist the implementation of
phylogenetic tip-dating tests using BEAST. Molecular Ecology Resources,
17: 608-613. <onlinelibrary.wiley.com/doi/full/10.1111/1755-0998.12603>.

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
%doc %{rlibdir}/%{packname}/example
%{rlibdir}/%{packname}/INDEX
