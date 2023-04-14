%global __brp_check_rpaths %{nil}
%global packname  rdi
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}%{?buildtag}
Summary:          Repertoire Dissimilarity Index

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-beanplot 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-beanplot 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-pdist 
Requires:         R-CRAN-stringr 

%description
Methods for calculation and visualization of the Repertoire Dissimilarity
Index. Citation: Bolen and Rubelt, et al (2017)
<doi:10.1186/s12859-017-1556-5>.

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
