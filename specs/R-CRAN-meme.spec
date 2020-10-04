%global packname  meme
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Create Meme

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridGraphics 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-grid 
Requires:         R-CRAN-gridGraphics 
Requires:         R-CRAN-magick 
Requires:         R-methods 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-sysfonts 
Requires:         R-utils 

%description
The word 'Meme' was originated from the book, 'The Selfish Gene', authored
by Richard Dawkins (1976). It is a unit of culture that is passed from one
generation to another and correlates to the gene, the unit of physical
heredity. The internet memes are captioned photos that are intended to be
funny, ridiculous. Memes behave like infectious viruses and travel from
person to person quickly through social media. The 'meme' package allows
users to make custom memes.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/angry8.jpg
%doc %{rlibdir}/%{packname}/ash-pikachu.0.0.jpg
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/fonts
%doc %{rlibdir}/%{packname}/icon.png
%doc %{rlibdir}/%{packname}/success.jpg
%{rlibdir}/%{packname}/INDEX
