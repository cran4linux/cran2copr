%global packname  asus
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Adaptive SURE Thresholding Using Side Information

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.2
Requires:         R-core >= 3.4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-rwt 
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rwt 
Requires:         R-CRAN-wavethresh 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides the ASUS procedure for estimating a high dimensional sparse
parameter in the presence of auxiliary data that encode side information
on sparsity. It is a robust data combination procedure in the sense that
even when pooling non-informative auxiliary data ASUS would be at least as
efficient as competing soft thresholding based methods that do not use
auxiliary data. For more information, please see the website
<http://www-bcf.usc.edu/~wenguans/Papers/ASUS.htm> and the accompanying
paper.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
