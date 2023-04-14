%global __brp_check_rpaths %{nil}
%global packname  pafdR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Book Companion for Processing and Analyzing Financial Data withR

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-exams 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-exams 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-curl 
Requires:         R-utils 
Requires:         R-stats 

%description
Provides access to material from the book "Processing and Analyzing
Financial Data with R" by Marcelo Perlin (2017) available at
<https://sites.google.com/view/pafdr/home>.

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
