%global packname  boundingbox
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Create a Bounding Box in an Image

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-gplots 
Requires:         R-CRAN-imager 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-CRAN-gplots 

%description
Generate ground truth cases for object localization algorithms. Cycle
through a list of images, select points around which to generate bounding
boxes and assign classifiers. Output the coordinates, and images annotated
with boxes and labels. For an example study that uses bounding boxes for
image localization and classification see Ibrahim, Badr, Abdallah, and
Eissa (2012) "Bounding Box Object Localization Based on Image
Superpixelization" <doi:10.1016/j.procs.2012.09.119>.

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
