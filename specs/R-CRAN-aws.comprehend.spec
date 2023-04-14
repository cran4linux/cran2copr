%global __brp_check_rpaths %{nil}
%global packname  aws.comprehend
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          3%{?dist}%{?buildtag}
Summary:          Client for 'AWS Comprehend'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-aws.signature >= 0.3.4
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-aws.signature >= 0.3.4
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 

%description
Client for 'AWS Comprehend' <https://aws.amazon.com/comprehend>, a cloud
natural language processing service that can perform a number of
quantitative text analyses, including language detection, sentiment
analysis, and feature extraction.

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
%{rlibdir}/%{packname}
