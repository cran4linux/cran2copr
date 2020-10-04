%global packname  papayar
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          View Medical Research Images using the Papaya JavaScript Library

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-servr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-utils 
Requires:         R-CRAN-neurobase 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-servr 
Requires:         R-CRAN-htmltools 
Requires:         R-utils 

%description
Users pass images and objects of class 'nifti' from the 'oro.nifti'
package to a Papaya, an interactive lightweight JavaScript viewer.
Although many packages can view individual slices or projections of image
and matrix data, this package allows for quick and easy interactive
browsing of images.  The viewer is based off of the Mango software, which
is a lightweight medical image viewer.

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
%doc %{rlibdir}/%{packname}/embed.html
%doc %{rlibdir}/%{packname}/index.html
%doc %{rlibdir}/%{packname}/papaya.css
%doc %{rlibdir}/%{packname}/papaya.js
%{rlibdir}/%{packname}/INDEX
