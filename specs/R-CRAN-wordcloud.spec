%global __brp_check_rpaths %{nil}
%global packname  wordcloud
%global packver   2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.6
Release:          3%{?dist}%{?buildtag}
Summary:          Word Clouds

License:          LGPL-2.1
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.9.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-CRAN-Rcpp >= 0.9.4
Requires:         R-methods 
Requires:         R-CRAN-RColorBrewer 

%description
Functionality to create pretty word clouds, visualize differences and
similarity between documents, and avoid over-plotting in scatter plots
with text.

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
