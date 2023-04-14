%global __brp_check_rpaths %{nil}
%global packname  DOT
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Render and Export DOT Graphs in R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-V8 >= 1.0
BuildRequires:    R-tools 
Requires:         R-CRAN-V8 >= 1.0
Requires:         R-tools 

%description
Renders DOT diagram markup language in R and also provides the possibility
to export the graphs in PostScript and SVG (Scalable Vector Graphics)
formats. In addition, it supports literate programming packages such as
'knitr' and 'rmarkdown'.

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
