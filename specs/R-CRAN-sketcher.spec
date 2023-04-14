%global __brp_check_rpaths %{nil}
%global packname  sketcher
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Pencil Sketch Effect

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-readbitmap 
BuildRequires:    R-CRAN-downloader 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-readbitmap 
Requires:         R-CRAN-downloader 
Requires:         R-CRAN-imager 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-dplyr 

%description
An implementation of image processing effects that convert a photo into a
line drawing image. For details, please refer to Tsuda, H. (2020).
sketcher: An R package for converting a photo into a sketch style image.
<doi:10.31234/osf.io/svmw5>.

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
