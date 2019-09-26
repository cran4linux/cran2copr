%global packname  IIS
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Datasets to Accompany Wolfe and Schneider - IntuitiveIntroductory Statistics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-asbio 
BuildRequires:    R-CRAN-BSDA 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-NSM3 
BuildRequires:    R-CRAN-Rfit 
Requires:         R-CRAN-asbio 
Requires:         R-CRAN-BSDA 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-NSM3 
Requires:         R-CRAN-Rfit 

%description
These datasets and functions accompany Wolfe and Schneider (2017) -
Intuitive Introductory Statistics (ISBN: 978-3-319-56070-0)
<http://www.springer.com/us/book/9783319560700>. They are used in the
examples throughout the text and in the end-of-chapter exercises. The
datasets are meant to cover a broad range of topics in order to appeal to
the diverse set of interests and backgrounds typically present in an
introductory Statistics class.

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
%{rlibdir}/%{packname}/INDEX
